---
url: https://docs.kicad.org/5.1/en/cvpcb/cvpcb.html
scraped_at: 2025-09-08T15:25:34.232118
title: Untitled
---

|  You actually **can** launch CvPcb from a stand alone Eeschema session
though, but please note that any schematic opened that does not have a project
file in the same path may be missing components due to missing libraries which
will not show up in CvPcb. If there is no fp-lib-table file in the same path
as the open schematic, no project specific footprint libraries will be
available either.

