# Events Over Time

Historical analysis of platform events and revenue.

```sql daily_revenue
select day, total_revenue 
from synthetic.daily_stats 
where event_type = 'purchase'
order by day
```

```sql events_trend
select day, event_type, event_count 
from synthetic.daily_stats
order by day
```

## Revenue Overview

<LineChart 
    data={daily_revenue} 
    x=day 
    y=total_revenue 
    title="Daily Revenue Trend"
    yFmt=currency
/>

## User Activity

<AreaChart 
    data={events_trend} 
    x=day 
    y=event_count 
    series=event_type 
    title="Daily Events by Type"
/>

## Detailed Stats

<DataTable data={events_trend} totalRow=true search=true />
