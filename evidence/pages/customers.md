# Customer Database

List of all registered customers on the platform.

```sql customers
select * from synthetic.customers
order by user_id
```

<DataTable data={customers} search=true rows=20>
  <Column id=user_id title="ID" />
  <Column id=name title="Name" />
  <Column id=email title="Email" />
  <Column id=country title="Country" />
</DataTable>
