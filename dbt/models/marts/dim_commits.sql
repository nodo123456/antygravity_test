
select
    id as event_id,
    type as event_type,
    actor__login as user_handle,
    repo__name as repo_name,
    created_at,
    -- Extract payload details if possible, depends on event type
    case 
        when type = 'PushEvent' then 'Push'
        when type = 'CreateEvent' then 'Create'
        else 'Other' 
    end as simple_type
from {{ source('raw_github', 'github_events') }}
