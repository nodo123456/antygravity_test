with source as (
    select * from {{ source('synthetic', 'raw_events') }}
),

cleaned as (
    select
        event_id,
        timestamp::timestamp as event_time,
        user_id,
        event_type,
        value::double as revenue
    from source
)

select * from cleaned
