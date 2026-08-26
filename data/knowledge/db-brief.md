# Database brief: recollect-local
Refreshed: 2026-08-26T12:33:51.731Z
Tables: 22

## Table index
- addresses :: address, created_at, id, label, user_id
- audit_events :: action, created_at, details, id, role, target_id, target_type, user_id
- circles :: code, created_at, geometry, id, name, updated_at, zone_id
- corporations :: created_at, id, name, updated_at
- escalation_rules :: channels, created_at, id, level, target_role, trigger_offset, updated_at
- escalations :: created_at, id, level, raised_by, reason, request_id
- flyway_schema_history :: checksum, description, execution_time, installed_by, installed_on, installed_rank, script, success, type, version
- invoices :: amount, circle_id, corporation_id, created_at, due_at, id, issued_at, month, rate_per_ton, request_count, status, tonnage
- notifications :: created_at, id, message, read, title, type, user_id
- payments :: amount, created_at, gst, id, method, request_id, status, total, txn_id, user_id
- photos :: captured_at, content_type, id, lat, lng, original_filename, request_id, size, stage, storage_key, url, user_id
- pricing_rules :: active, base_rate, created_at, effective_from, effective_to, gst_rate, id, updated_at
- request_code_sequence :: id, last_val, prefix, version, year
- status_flows :: created_at, id, status, step_order, terminal, updated_at
- tat_rules :: breach_action, created_at, id, request_type, tat_hours, updated_at, warning_hours
- transfer_stations :: address, capacity_tons, contact, created_at, days, hours, id, lat, lng, name, pricing_per_ton, status, updated_at, used_tons
- users :: agency, avatar_url, capacity, circle_id, created_at, deleted_at, driver_status, email, employee_id, id, mobile, name, password_hash, role, status, updated_at, vehicle, vehicle_type
- vehicle_types :: available, created_at, icon, id, max_capacity, min_capacity, price_per_ton, type, updated_at
- wards :: circle_id, code, created_at, geometry, id, name, updated_at
- waste_requests :: actual_weight, address, agency, amount, circle_id, citizen_name, created_at, created_by, deleted_at, driver_id, estimated_weight, gross_weight, gst, id, latitude, location, longitude, mobile, notes, payment_status, pickup_date, request_code, service_type, status, tare_weight, tat_status, total, transfer_station_id, txn_id, type, updated_at, variance_pct, vehicle, verify_remarks, ward_id, waste_type, zone_id
- weighments :: captured_at, gross_weight, id, net_weight, request_id, tare_weight, weighbridge_id, weighment_ref
- zones :: code, corporation_id, created_at, geometry, id, name, updated_at

## Relationships
- addresses.user_id -> users.id
- audit_events.user_id -> users.id
- circles.zone_id -> zones.id
- invoices.circle_id -> circles.id
- invoices.corporation_id -> corporations.id
- notifications.user_id -> users.id
- payments.request_id -> waste_requests.id
- payments.user_id -> users.id
- photos.request_id -> waste_requests.id
- users.circle_id -> circles.id
- wards.circle_id -> circles.id
- waste_requests.circle_id -> circles.id
- waste_requests.driver_id -> users.id
- waste_requests.transfer_station_id -> transfer_stations.id
- waste_requests.ward_id -> wards.id
- waste_requests.zone_id -> zones.id
- weighments.request_id -> waste_requests.id
- zones.corporation_id -> corporations.id

## Table data

### addresses (0 rows)
columns: address, created_at, id, label, user_id
empty

### audit_events (0 rows)
columns: action, created_at, details, id, role, target_id, target_type, user_id
empty

### circles (16 rows)
columns: code, created_at, geometry, id, name, updated_at, zone_id
id=1; zone_id=1; code=C1; name=Circle 1 - Miyapur; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; zone_id=1; code=C2; name=Circle 2 - Chandanagar; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; zone_id=1; code=C3; name=Circle 3 - Kondapur; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=4; zone_id=1; code=C4; name=Circle 4 - Gachibowli; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=5; zone_id=1; code=C5; name=Circle 5 - Manikonda; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=6; zone_id=1; code=C6; name=Circle 6 - Serilingampally; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=7; zone_id=2; code=C7; name=Circle 7 - Rajendranagar; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=8; zone_id=2; code=C8; name=Circle 8 - Attapur; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=9; zone_id=2; code=C9; name=Circle 9 - Mehdipatnam; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=10; zone_id=2; code=C10; name=Circle 10 - Shamshabad; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=11; zone_id=2; code=C11; name=Circle 11 - Moinabad; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=12; zone_id=3; code=C12; name=Circle 12 - Balanagar; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=13; zone_id=3; code=C13; name=Circle 13 - Kukatpally; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=14; zone_id=3; code=C14; name=Circle 14 - Moosapet; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=15; zone_id=3; code=C15; name=Circle 15 - Qutbullapur; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=16; zone_id=3; code=C16; name=Circle 16 - KPHB; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### corporations (1 rows)
columns: created_at, id, name, updated_at
id=1; name=Cyberabad Municipal Corporation; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### escalation_rules (3 rows)
columns: channels, created_at, id, level, target_role, trigger_offset, updated_at
id=1; level=L1; trigger_offset=TAT+2h; target_role=RESL; channels=SMS,EMAIL; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; level=L2; trigger_offset=TAT+6h; target_role=RESL; channels=SMS,EMAIL,PUSH; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; level=L3; trigger_offset=TAT+12h; target_role=ADMIN; channels=EMAIL,REPORT; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### escalations (0 rows)
columns: created_at, id, level, raised_by, reason, request_id
empty

### flyway_schema_history (3 rows)
columns: checksum, description, execution_time, installed_by, installed_on, installed_rank, script, success, type, version
installed_rank=1; version=1.0.0; description=create tables; type=SQL; script=V1.0.0__create_tables.sql; checksum=-657842069; installed_by=root; installed_on=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); execution_time=1275; success=1
installed_rank=2; version=1.0.1; description=seed reference data; type=SQL; script=V1.0.1__seed_reference_data.sql; checksum=-490638521; installed_by=root; installed_on=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); execution_time=244; success=1
installed_rank=3; version=1.0.2; description=seed e2e flow data; type=SQL; script=V1.0.2__seed_e2e_flow_data.sql; checksum=1053690582; installed_by=root; installed_on=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); execution_time=39; success=1

### invoices (0 rows)
columns: amount, circle_id, corporation_id, created_at, due_at, id, issued_at, month, rate_per_ton, request_count, status, tonnage
empty

### notifications (0 rows)
columns: created_at, id, message, read, title, type, user_id
empty

### payments (0 rows)
columns: amount, created_at, gst, id, method, request_id, status, total, txn_id, user_id
empty

### photos (0 rows)
columns: captured_at, content_type, id, lat, lng, original_filename, request_id, size, stage, storage_key, url, user_id
empty

### pricing_rules (1 rows)
columns: active, base_rate, created_at, effective_from, effective_to, gst_rate, id, updated_at
id=1; base_rate=450.00; gst_rate=18.00; effective_from=Mon Jan 01 2024 00:00:00 GMT+0530 (India Standard Time); active=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### request_code_sequence (0 rows)
columns: id, last_val, prefix, version, year
empty

### status_flows (20 rows)
columns: created_at, id, status, step_order, terminal, updated_at
id=1; status=DRAFT; step_order=1; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; status=SUBMITTED; step_order=2; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; status=PAYMENT_PENDING; step_order=3; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=4; status=PAYMENT_CONFIRMED; step_order=4; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=5; status=UNDER_REVIEW; step_order=5; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=6; status=ACCEPTED; step_order=6; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=7; status=REJECTED; terminal=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=8; status=LOGISTICS_ASSIGNED; step_order=7; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=9; status=LOGISTICS_ACCEPTED; step_order=8; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=10; status=EN_ROUTE; step_order=9; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=11; status=ARRIVED; step_order=10; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=12; status=WASTE_COLLECTED; step_order=11; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=13; status=AT_TRANSFER_STATION; step_order=12; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=14; status=WEIGHED; step_order=13; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=15; status=AWAITING_VERIFICATION; step_order=14; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=16; status=COMPLETED; step_order=15; terminal=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=17; status=CLOSED; terminal=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=18; status=CANCELLED; terminal=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=19; status=REOPENED; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=20; status=ESCALATED; terminal= ; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### tat_rules (2 rows)
columns: breach_action, created_at, id, request_type, tat_hours, updated_at, warning_hours
id=1; request_type=CLAIMED; tat_hours=72.0; warning_hours=12.0; breach_action=AUTO_ESCALATE; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; request_type=UNCLAIMED; tat_hours=120.0; warning_hours=24.0; breach_action=AUTO_ESCALATE; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### transfer_stations (6 rows)
columns: address, capacity_tons, contact, created_at, days, hours, id, lat, lng, name, pricing_per_ton, status, updated_at, used_tons
id=1; name=Gachibowli TS; address=Gachibowli, Hyderabad; status=OPEN; capacity_tons=500.0; used_tons=120.0; pricing_per_ton=450.00; lat=17.440000; lng=78.350000; contact=040-2300; hours=06:00-22:00; days=All
id=2; name=Miyapur TS; address=Miyapur, Telangana, India; status=OPEN; capacity_tons=400.0; used_tons=90.0; pricing_per_ton=450.00; lat=17.516901; lng=78.342830; contact=040-2400; hours=06:00-22:00; days=All
id=3; name=Rajendranagar TS; address=Gachibowli, Hyderabad, Telangana, India; status=OPEN; capacity_tons=350.0; used_tons=60.0; pricing_per_ton=450.00; lat=17.440080; lng=78.348917; contact=040-2500; hours=06:00-22:00; days=All
id=4; name=Balanagar TS; address=Balanagar, Hyderabad; status=CLOSED; capacity_tons=300.0; used_tons=0.0; pricing_per_ton=450.00; lat=17.480000; lng=78.400000; contact=040-2600; hours=06:00-22:00; days=All
id=2092253151745937400; name=Test; address=VINDHYA HILLS, Pragathi Nagar, Hyderabad, Telangana 500090, India; status=OPEN; capacity_tons=1.0; used_tons=34.0; pricing_per_ton=345.00; lat=17.521408; lng=78.398218; contact=987654321; hours=06:00-22:00; days=All
id=2092242985755480000; name=string; address=string; status=OPEN; capacity_tons=0.0; used_tons=0.0; pricing_per_ton=0.00; lat=0.000000; lng=0.000000; contact=string; hours=string; days=string

### users (6 rows)
columns: agency, avatar_url, capacity, circle_id, created_at, deleted_at, driver_status, email, employee_id, id, mobile, name, password_hash, role, status, updated_at, vehicle, vehicle_type
id=1; name=Demo Citizen; mobile=919876543210; role=CITIZEN; status=ACTIVE; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; name=Demo AMOH; mobile=919876543299; role=AMOH; status=ACTIVE; employee_id=CMC-AMH-0001; circle_id=10; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; name=Demo Driver; mobile=918765432109; role=DRIVER; status=ACTIVE; vehicle=Tata Ace; vehicle_type=Mini Truck; capacity=1.5T; agency=RESL Logistics; driver_status=AVAILABLE; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=4; name=Demo RESL; password_hash=$2y$10$dcYga0zEUKoSa0rleFtzkutwim0KJYqJajz1fEJmrdGnrc8dZ01TS; role=RESL; status=ACTIVE; employee_id=RESL-0001; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=5; name=Demo Admin; password_hash=$2y$10$dcYga0zEUKoSa0rleFtzkutwim0KJYqJajz1fEJmrdGnrc8dZ01TS; role=ADMIN; status=ACTIVE; employee_id=ADM-0001; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=6; name=Demo CMC; password_hash=$2y$10$dcYga0zEUKoSa0rleFtzkutwim0KJYqJajz1fEJmrdGnrc8dZ01TS; role=CMC; status=ACTIVE; employee_id=CMC-0001; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### vehicle_types (7 rows)
columns: available, created_at, icon, id, max_capacity, min_capacity, price_per_ton, type, updated_at
id=1; type=string; min_capacity=0.00; max_capacity=0.00; price_per_ton=0.00; icon=tractor; available=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 07:52:45 GMT+0530 (India Standard Time)
id=2; type=Mini Truck; min_capacity=1.00; max_capacity=4.00; price_per_ton=450.00; icon=truck; available=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; type=Tipper; min_capacity=4.00; max_capacity=10.00; price_per_ton=600.00; icon=tipper; available=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=4; type=Container; min_capacity=10.00; max_capacity=20.10; price_per_ton=900.00; icon=container; available=; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 07:55:10 GMT+0530 (India Standard Time)
id=2092241943378661400; type=test; min_capacity=1.00; max_capacity=33.00; price_per_ton=12.00; available=; created_at=Tue Aug 25 2026 07:55:25 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 07:55:25 GMT+0530 (India Standard Time)
id=2092238647901425700; type=Tipper; min_capacity=0.00; max_capacity=0.00; price_per_ton=0.00; available=; created_at=Tue Aug 25 2026 07:42:20 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 07:42:20 GMT+0530 (India Standard Time)
id=2092238066164043800; type=string; min_capacity=0.00; max_capacity=0.00; price_per_ton=0.00; available=; created_at=Tue Aug 25 2026 07:40:01 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 07:40:01 GMT+0530 (India Standard Time)

### wards (76 rows)
columns: circle_id, code, created_at, geometry, id, name, updated_at
id=1; circle_id=1; code=W1; name=Ward 1; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; circle_id=2; code=W2; name=Ward 2; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; circle_id=3; code=W3; name=Ward 3; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=4; circle_id=4; code=W4; name=Ward 4; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=5; circle_id=5; code=W5; name=Ward 5; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=6; circle_id=6; code=W6; name=Ward 6; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=7; circle_id=7; code=W7; name=Ward 7; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=8; circle_id=8; code=W8; name=Ward 8; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=9; circle_id=9; code=W9; name=Ward 9; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=10; circle_id=10; code=W10; name=Ward 10; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=11; circle_id=11; code=W11; name=Ward 11; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=12; circle_id=12; code=W12; name=Ward 12; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=13; circle_id=13; code=W13; name=Ward 13; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=14; circle_id=14; code=W14; name=Ward 14; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=15; circle_id=15; code=W15; name=Ward 15; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=16; circle_id=16; code=W16; name=Ward 16; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=17; circle_id=1; code=W17; name=Ward 17; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=18; circle_id=2; code=W18; name=Ward 18; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=19; circle_id=3; code=W19; name=Ward 19; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=20; circle_id=4; code=W20; name=Ward 20; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=21; circle_id=5; code=W21; name=Ward 21; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=22; circle_id=6; code=W22; name=Ward 22; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=23; circle_id=7; code=W23; name=Ward 23; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=24; circle_id=8; code=W24; name=Ward 24; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=25; circle_id=9; code=W25; name=Ward 25; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=26; circle_id=10; code=W26; name=Ward 26; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=27; circle_id=11; code=W27; name=Ward 27; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=28; circle_id=12; code=W28; name=Ward 28; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=29; circle_id=13; code=W29; name=Ward 29; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=30; circle_id=14; code=W30; name=Ward 30; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=31; circle_id=15; code=W31; name=Ward 31; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=32; circle_id=16; code=W32; name=Ward 32; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=33; circle_id=1; code=W33; name=Ward 33; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=34; circle_id=2; code=W34; name=Ward 34; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=35; circle_id=3; code=W35; name=Ward 35; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=36; circle_id=4; code=W36; name=Ward 36; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=37; circle_id=5; code=W37; name=Ward 37; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=38; circle_id=6; code=W38; name=Ward 38; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=39; circle_id=7; code=W39; name=Ward 39; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=40; circle_id=8; code=W40; name=Ward 40; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=41; circle_id=9; code=W41; name=Ward 41; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=42; circle_id=10; code=W42; name=Ward 42; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=43; circle_id=11; code=W43; name=Ward 43; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=44; circle_id=12; code=W44; name=Ward 44; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=45; circle_id=13; code=W45; name=Ward 45; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=46; circle_id=14; code=W46; name=Ward 46; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=47; circle_id=15; code=W47; name=Ward 47; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=48; circle_id=16; code=W48; name=Ward 48; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=49; circle_id=1; code=W49; name=Ward 49; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=50; circle_id=2; code=W50; name=Ward 50; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=51; circle_id=3; code=W51; name=Ward 51; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=52; circle_id=4; code=W52; name=Ward 52; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=53; circle_id=5; code=W53; name=Ward 53; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=54; circle_id=6; code=W54; name=Ward 54; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=55; circle_id=7; code=W55; name=Ward 55; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=56; circle_id=8; code=W56; name=Ward 56; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=57; circle_id=9; code=W57; name=Ward 57; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=58; circle_id=10; code=W58; name=Ward 58; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=59; circle_id=11; code=W59; name=Ward 59; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=60; circle_id=12; code=W60; name=Ward 60; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=61; circle_id=13; code=W61; name=Ward 61; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=62; circle_id=14; code=W62; name=Ward 62; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=63; circle_id=15; code=W63; name=Ward 63; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=64; circle_id=16; code=W64; name=Ward 64; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=65; circle_id=1; code=W65; name=Ward 65; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=66; circle_id=2; code=W66; name=Ward 66; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=67; circle_id=3; code=W67; name=Ward 67; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=68; circle_id=4; code=W68; name=Ward 68; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=69; circle_id=5; code=W69; name=Ward 69; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=70; circle_id=6; code=W70; name=Ward 70; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=71; circle_id=7; code=W71; name=Ward 71; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=72; circle_id=8; code=W72; name=Ward 72; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=73; circle_id=9; code=W73; name=Ward 73; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=74; circle_id=10; code=W74; name=Ward 74; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=75; circle_id=11; code=W75; name=Ward 75; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=76; circle_id=12; code=W76; name=Ward 76; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)

### waste_requests (0 rows)
columns: actual_weight, address, agency, amount, circle_id, citizen_name, created_at, created_by, deleted_at, driver_id, estimated_weight, gross_weight, gst, id, latitude, location, longitude, mobile, notes, payment_status, pickup_date, request_code, service_type, status, tare_weight, tat_status, total, transfer_station_id, txn_id, type, updated_at, variance_pct, vehicle, verify_remarks, ward_id, waste_type, zone_id
empty

### weighments (0 rows)
columns: captured_at, gross_weight, id, net_weight, request_id, tare_weight, weighbridge_id, weighment_ref
empty

### zones (3 rows)
columns: code, corporation_id, created_at, geometry, id, name, updated_at
id=1; corporation_id=1; code=Z1; name=Zone 1 - Serilingampally; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=2; corporation_id=1; code=Z2; name=Zone 2 - Rajendranagar; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
id=3; corporation_id=1; code=Z3; name=Zone 3 - Balanagar; geometry=[object Object],[object Object],[object Object],[object Object],[object Object]; created_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time); updated_at=Tue Aug 25 2026 17:45:52 GMT+0530 (India Standard Time)
