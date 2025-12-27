with source as (
    select * from {{ source('synthetic', 'raw_customers') }}
),

cleaned as (
    select
        user_id,
        name,
        email,
        country
    from source
)

select * from cleaned
