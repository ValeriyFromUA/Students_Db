define USAGE
Commands:
	run_db      Run main database
	run_test_db Run test database
	run_db_init Run both databases
	run_web		Run web appliaction
	run_app		Run databases and web appliaction
	check		Test appliaction code with isort and flake8
	create_data Add data to database
	test		Run tests
endef

run_db:
	docker-compose up -d db

run_test_db:
	docker-compose up -d test-db

run_db_init: run_db run_test_db

run_web:
	docker-compose up web

run_web_s:
	docker-compose up -d web

run_app: run_db run_test_db run_web

isort:
	isort --check-only .

flake:
	flake8 --show-source .

check: run_web_s isort flake

create_data:
	docker-compose up -d db
	docker-compose run --rm web python create_db_with_data.py

test:
	docker-compose up -d test-db
	docker-compose run --rm web pytest -v
