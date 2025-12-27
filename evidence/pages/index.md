# My Data Dashboard

This dashboard visualizes data from our verified CSV source.

```sql my_data
select * from demo.test_table
```

<BarChart 
    data={my_data} 
    x=message 
    y=value 
    title="Demo Values"
/>

<DataTable data={my_data} />
