CREATE TABLE task1.request_history(
id  integer PRIMARY KEY GENERATED BY DEFAULT AS IDENTITY,
data_source varchar(300),
load_dttm timestamp DEFAULT current_timestamp,
batch_sze integer
   );

