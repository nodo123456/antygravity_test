with customers as (
    select * from {{ ref('stg_customers') }}
),

events as (
    select * from {{ ref('stg_events') }}
),

customer_stats as (
    select
        user_id,
        count(*) as total_events,
        sum(revenue) as total_revenue,
        max(event_time) as last_active_at
    from events
    group by 1
),

final as (
    select
        c.user_id,
        c.name,
        c.email,
        c.country,
        coalesce(s.total_events, 0) as total_events,
        coalesce(s.total_revenue, 0) as total_revenue,
        s.last_active_at,
        case 
            when s.total_events > 0 then 'Active' 
            else 'Inactive' 
        end as status
    from customers c
    left join customer_stats s on c.user_id = s.user_id
)

select * from final
order by total_revenue desc nulls last
