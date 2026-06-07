import React, { useState } from 'react'
import { CompactMarkdown } from '@/components/chat/compact-markdown'
import { ChevronLeft, ChevronRight } from 'lucide-react'
import { cn } from '@/lib/utils'

interface MarkdownCarouselProps {
  code: string
  defer?: boolean
}

export const MarkdownCarousel: React.FC<MarkdownCarouselProps> = ({ code, defer }) => {
  const [currentIndex, setCurrentIndex] = useState(0)

  // Split slides by the HTML comment
  const slides = code.split('<!-- slide -->').map(s => s.trim()).filter(s => s.length > 0)

  if (defer || slides.length === 0) {
    return (
      <div className="flex animate-pulse items-center justify-center rounded-md border border-border bg-muted/20 p-6 text-sm text-muted-foreground">
        Loading carousel...
      </div>
    )
  }

  const handleNext = () => setCurrentIndex(prev => (prev + 1) % slides.length)
  const handlePrev = () => setCurrentIndex(prev => (prev - 1 + slides.length) % slides.length)

  return (
    <div className="aui-carousel my-4 overflow-hidden rounded-xl border border-border bg-card shadow-sm">
      {/* Carousel Content */}
      <div className="relative p-6">
        <CompactMarkdown className="wrap-anywhere" text={slides[currentIndex]} />
      </div>

      {/* Controls */}
      {slides.length > 1 && (
        <div className="flex items-center justify-between border-t border-border bg-muted/30 px-4 py-2">
          <button
            onClick={handlePrev}
            className="flex size-8 items-center justify-center rounded-full hover:bg-muted"
            aria-label="Previous slide"
          >
            <ChevronLeft className="size-4" />
          </button>
          
          <div className="flex gap-1.5">
            {slides.map((_, idx) => (
              <button
                key={idx}
                onClick={() => setCurrentIndex(idx)}
                className={cn(
                  "size-2 rounded-full transition-colors",
                  idx === currentIndex ? "bg-primary" : "bg-muted-foreground/30 hover:bg-muted-foreground/50"
                )}
                aria-label={`Go to slide ${idx + 1}`}
              />
            ))}
          </div>

          <button
            onClick={handleNext}
            className="flex size-8 items-center justify-center rounded-full hover:bg-muted"
            aria-label="Next slide"
          >
            <ChevronRight className="size-4" />
          </button>
        </div>
      )}
    </div>
  )
}
