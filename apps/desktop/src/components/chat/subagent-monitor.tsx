import { useEffect, useState } from 'react'
import { getSubagents } from '@/hermes'
import type { SubagentJob } from '@/types/hermes'
import { Activity, Clock, FolderGit2 } from 'lucide-react'
import { Badge } from '@/components/ui/badge'
import { ScrollArea } from '@/components/ui/scroll-area'

export function SubagentMonitor() {
  const [jobs, setJobs] = useState<Record<string, SubagentJob>>({})

  useEffect(() => {
    let mounted = true
    const poll = async () => {
      try {
        const res = await getSubagents()
        if (mounted && res?.data) {
          setJobs(res.data)
        }
      } catch (err) {
        console.error('Failed to fetch subagents', err)
      }
    }

    poll()
    const interval = setInterval(poll, 3000)
    return () => {
      mounted = false
      clearInterval(interval)
    }
  }, [])

  const jobEntries = Object.entries(jobs)
  if (jobEntries.length === 0) {
    return null
  }

  return (
    <div className="flex flex-col gap-2 p-3 border rounded-md bg-muted/20">
      <div className="flex items-center gap-2 mb-1">
        <Activity className="w-4 h-4 text-primary" />
        <h3 className="text-sm font-medium">Active Subagents ({jobEntries.length})</h3>
      </div>
      <ScrollArea className="max-h-[250px]">
        <div className="flex flex-col gap-2">
          {jobEntries.map(([id, job]) => (
            <div key={id} className="flex flex-col p-2 text-xs border rounded-md bg-background gap-1.5">
              <div className="flex items-center justify-between">
                <span className="font-mono text-[10px] text-muted-foreground truncate" title={id}>{id}</span>
                <Badge variant={job.status === 'running' ? 'default' : 'muted'}>
                  {job.status}
                </Badge>
              </div>
              <div className="flex items-center gap-2 text-muted-foreground">
                <Clock className="w-3 h-3 shrink-0" />
                <span>{new Date(job.start_time * 1000).toLocaleTimeString()}</span>
              </div>
              {job.workspace_dir && (
                <div className="flex items-center gap-2 text-muted-foreground">
                  <FolderGit2 className="w-3 h-3 shrink-0" />
                  <span className="truncate" title={job.workspace_dir}>{job.workspace_dir}</span>
                </div>
              )}
            </div>
          ))}
        </div>
      </ScrollArea>
    </div>
  )
}
