import React, { useEffect, useRef, useState } from 'react'
import mermaid from 'mermaid'

// Initialize mermaid
mermaid.initialize({
  startOnLoad: false,
  theme: 'default',
  securityLevel: 'loose'
})

interface MarkdownMermaidProps {
  code: string
  defer?: boolean
}

export const MarkdownMermaid: React.FC<MarkdownMermaidProps> = ({ code, defer }) => {
  const containerRef = useRef<HTMLDivElement>(null)
  const [svgContent, setSvgContent] = useState<string>('')
  const [error, setError] = useState<string | null>(null)

  useEffect(() => {
    // If we're deferring/streaming, don't try to render partial mermaid code
    if (defer || !code.trim()) return

    const renderMermaid = async () => {
      try {
        setError(null)
        // Generate a unique ID for this diagram
        const id = `mermaid-${Math.random().toString(36).substr(2, 9)}`
        const { svg } = await mermaid.render(id, code)
        setSvgContent(svg)
      } catch (err: any) {
        console.error("Mermaid rendering error", err)
        setError(err?.message || "Failed to render Mermaid diagram")
      }
    }

    renderMermaid()
  }, [code, defer])

  if (defer) {
    return (
      <div className="flex animate-pulse items-center justify-center rounded-md border border-border bg-muted/20 p-6 text-sm text-muted-foreground">
        Drawing diagram...
      </div>
    )
  }

  if (error) {
    return (
      <div className="rounded-md border border-destructive/50 bg-destructive/10 p-4 text-sm text-destructive">
        <strong>Mermaid Error:</strong>
        <pre className="mt-2 whitespace-pre-wrap text-xs">{error}</pre>
        <pre className="mt-2 whitespace-pre-wrap text-xs text-muted-foreground">{code}</pre>
      </div>
    )
  }

  return (
    <div
      ref={containerRef}
      className="aui-mermaid my-4 flex justify-center overflow-x-auto rounded-md bg-white p-4"
      dangerouslySetInnerHTML={{ __html: svgContent }}
    />
  )
}
