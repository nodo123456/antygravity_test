---
title: My Modern Data Stack
---

```sql commits_by_type
select 
    simple_type,
    count(*) as commit_count
from my_project.dim_commits
group by all
order by commit_count desc
```

# GitHub Activity Analysis
This dashboard is built automatically using **dlt**, **DuckDB**, **dbt**, and **Evidence**.

<BarChart 
    data={commits_by_type}
    x=simple_type
    y=commit_count
    title="Events by Type"
/>

## Recent Events
```sql recent_events
select * from my_project.dim_commits order by created_at desc limit 10
```

<DataTable data={recent_events} />
