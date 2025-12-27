with events as (
    select * from {{ ref('stg_events') }}
),

daily as (
    select
        date_trunc('day', event_time) as day,
        event_type,
        count(*) as event_count,
        sum(revenue) as total_revenue,
        count(distinct user_id) as active_users
    from events
    group by 1, 2
)

select * from daily
order by day desc, total_revenue desc
