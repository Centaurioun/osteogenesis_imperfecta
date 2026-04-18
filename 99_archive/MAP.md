# 99_archive Map

```text
99_archive/
├─ by_release/                 # lineage-based archival buckets
├─ by_date/                    # reorg wave/date snapshots
├─ snapshots/                  # root inventory + move logs
└─ indexes/
   └─ archive_lookup.csv       # original->archive path mapping
```

Archive policy: no-delete, append-only provenance logs.
