# Masters and keys
Database: recollect-local
Tables: 22

## Master tables (most referenced)
- users | pk: id | referenced by 5 tables
- circles | pk: id | referenced by 4 tables
- waste requests | pk: id | referenced by 3 tables

## Relationships
- addresses.user_id -> users.id
- audit events.user_id -> users.id
- circles.zone_id -> zones.id
- invoices.circle_id -> circles.id
- invoices.corporation_id -> corporations.id
- notifications.user_id -> users.id
- payments.request_id -> waste requests.id
- payments.user_id -> users.id
- photos.request_id -> waste requests.id
- users.circle_id -> circles.id
- wards.circle_id -> circles.id
- waste requests.circle_id -> circles.id
- waste requests.driver_id -> users.id
- waste requests.transfer_station_id -> transfer stations.id
- waste requests.ward_id -> wards.id
- waste requests.zone_id -> zones.id
- weighments.request_id -> waste requests.id
- zones.corporation_id -> corporations.id
