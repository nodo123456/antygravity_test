# Customer Database

List of all registered customers on the platform.

```sql q_status_options
select 'All' as status 
union all 
select distinct status from synthetic.customer_activity
order by status
```

<Dropdown name=status_filter title="Status" data={q_status_options} label=status value=status defaultValue="All" />

```sql customers
select 
    user_id, 
    name, 
    email, 
    country, 
    total_events, 
    total_revenue, 
    status 
from synthetic.customer_activity
where ('${inputs.status_filter}' = 'All' OR status = '${inputs.status_filter}')
order by total_revenue desc
```

## Customer Activity

<DataTable data={customers} search=true rows=20>
  <Column id=user_id title="ID" />
  <Column id=name title="Name" />
  <Column id=country title="Country" />
  <Column id=status title="Status" />
  <Column id=total_events title="Events" />
  <Column id=total_revenue title="Lifetime Value" fmt=currency />
</DataTable>
