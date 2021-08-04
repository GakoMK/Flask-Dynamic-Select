# Python Flask Dynamic Select Box using Flask-WTF, javascript and SQLAlchemy
Based on: https://tutorial101.blogspot.com/2020/04/python-flask-dynamic-select-box-using.html

### Start:
```
flask db init
flask db migrate
flask db upgrade / downgrade
```

### DB:
```
INSERT INTO countries (id, name) VALUES (1, 'Poland');
INSERT INTO countries (id, name) VALUES (2, 'Italy');
```
```
INSERT INTO state (id, name, country_id) VALUES (1, 'Lesser Poland', 1);
INSERT INTO state (id, name, country_id) VALUES (2, 'Choose me ID2', 1);
INSERT INTO state (id, name, country_id) VALUES (3, 'Silesia', 1);
INSERT INTO state (id, name, country_id) VALUES (4, 'Masovia', 1);
INSERT INTO state (id, name, country_id) VALUES (5, 'Abruzzo', 2);
INSERT INTO state (id, name, country_id) VALUES (6, 'Choose me ID6', 2);
INSERT INTO state (id, name, country_id) VALUES (7, 'Campania', 2);
```
```
INSERT INTO city (id, state, name, stateid) VALUES (1, 'CA', 'City 1 for id 6', 6);
INSERT INTO city (id, state, name, stateid) VALUES (2, 'NV', 'City 2 for id6', 6);
INSERT INTO city (id, state, name, stateid) VALUES (3, 'CA', 'City 3 for id6', 6);
INSERT INTO city (id, state, name, stateid) VALUES (4, NULL, 'City 1 for id2', 2);
INSERT INTO city (id, state, name, stateid) VALUES (5, 'NULL', 'City 2 for id2', 2);
INSERT INTO city (id, state, name, stateid) VALUES (6, NULL, 'City 3 for id2', 2);
```

### Run:
```
python main.py
```
