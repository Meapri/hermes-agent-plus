import React, { ComponentProps, ReactNode } from 'react'
import { Info, AlertTriangle, Lightbulb, AlertCircle, Flame } from 'lucide-react'
import { cn } from '@/lib/utils'

// Helper to recursively extract text from React nodes
function extractText(node: ReactNode): string {
  if (typeof node === 'string') return node
  if (typeof node === 'number') return String(node)
  if (Array.isArray(node)) return node.map(extractText).join('')
  if (React.isValidElement(node) && node.props && typeof node.props === 'object' && 'children' in node.props) {
    return extractText((node.props as any).children)
  }
  return ''
}

export function MarkdownAlert({ className, children, ...props }: ComponentProps<'blockquote'>) {
  const textContent = extractText(children)
  
  // Check if it matches GitHub alert syntax
  const match = textContent.match(/^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i)
  
  if (!match) {
    // Not an alert, render as standard blockquote
    return (
      <blockquote
        className={cn('border-l-2 border-border pl-3 text-muted-foreground italic', className)}
        {...props}
      >
        {children}
      </blockquote>
    )
  }

  const alertType = match[1].toUpperCase()
  
  // Strip the [!TYPE] from the children to render the body cleanly
  // Since children can be complex React nodes, we do a simple string replace on the first matching text node.
  const stripAlertTag = (nodes: ReactNode): ReactNode => {
    if (typeof nodes === 'string') {
      return nodes.replace(/^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i, '').trim()
    }
    if (Array.isArray(nodes)) {
      let found = false
      return nodes.map(node => {
        if (!found && typeof node === 'string' && node.match(/^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i)) {
          found = true
          return stripAlertTag(node)
        }
        if (!found && React.isValidElement(node)) {
          // If the text is inside a paragraph
          const childText = extractText(node)
          if (childText.match(/^\[!(NOTE|TIP|IMPORTANT|WARNING|CAUTION)\]/i)) {
            found = true
            const element = node as React.ReactElement<any>
            return React.cloneElement(element, {
              ...element.props,
              children: stripAlertTag(element.props.children)
            })
          }
        }
        return node
      })
    }
    if (React.isValidElement(nodes)) {
      const element = nodes as React.ReactElement<any>
      return React.cloneElement(element, {
        ...element.props,
        children: stripAlertTag(element.props.children)
      })
    }
    return nodes
  }

  const cleanedChildren = stripAlertTag(children)

  let icon = <Info className="size-4" />
  let title = "Note"
  let colorClass = "border-blue-500/50 bg-blue-500/10 text-blue-600 dark:text-blue-400"

  switch (alertType) {
    case 'TIP':
      icon = <Lightbulb className="size-4" />
      title = "Tip"
      colorClass = "border-green-500/50 bg-green-500/10 text-green-600 dark:text-green-400"
      break
    case 'IMPORTANT':
      icon = <AlertCircle className="size-4" />
      title = "Important"
      colorClass = "border-purple-500/50 bg-purple-500/10 text-purple-600 dark:text-purple-400"
      break
    case 'WARNING':
      icon = <AlertTriangle className="size-4" />
      title = "Warning"
      colorClass = "border-amber-500/50 bg-amber-500/10 text-amber-600 dark:text-amber-400"
      break
    case 'CAUTION':
      icon = <Flame className="size-4" />
      title = "Caution"
      colorClass = "border-red-500/50 bg-red-500/10 text-red-600 dark:text-red-400"
      break
  }

  // Separate div-incompatible props (like cite) from the rest
  const { cite, ...divProps } = props as any

  return (
    <div className={cn("aui-alert my-4 rounded-md border-l-4 p-4", colorClass, className)} {...divProps}>
      <div className="mb-1 flex items-center gap-2 font-semibold">
        {icon}
        <span>{title}</span>
      </div>
      <div className="text-sm opacity-90 [&>*:first-child]:mt-0 [&>*:last-child]:mb-0">
        {cleanedChildren}
      </div>
    </div>
  )
}
