import uuid

from tabulate import tabulate


def load_csv_logfile(log_file_path):
    columns = []
    log_data = {}
    event_types = set()
    try:
        log_file = open(log_file_path, encoding='utf-8-sig')
    except FileNotFoundError:
        print('no file')
    else:
        i = 0
        current_uuid = ''
        try:
            for current_line in log_file:
                if i == 0:  # From first row we grab the titles
                    columns = current_line.strip().split(',')
                    columns.append('Описание')  # Missing column title
                else:
                    partitioned_line = current_line.strip().split(',')
                    if len(partitioned_line) == 6:  # It's header string
                        # Separate set for event types
                        event_types.add(partitioned_line[0])
                        # New event - new UUID
                        current_uuid = uuid.uuid4().hex
                        # Add dictionary record (list) with UUID key
                        log_data[current_uuid] = [partitioned_line]
                    else:
                        # Append linked log rows as list elements
                        log_data[current_uuid].append(partitioned_line)
                i += 1
        finally:
            log_file.close()
    return [columns, log_data, event_types]


columns_list, log_data, event_types = \
    load_csv_logfile('/home/tuod/system_log.csv')

event_types_tabular = list(map(lambda x: [x], sorted(event_types)))

print(tabulate(tabular_data=event_types_tabular,
               headers=['Тип события'],
               tablefmt='grid'))


def get_events_by_event_type(event_type: str = 'Сведения') -> list:
    events_by_event_type_list = []
    for events in log_data.keys():
        if log_data[events][0][0] == event_type:
            # Last column is too long
            events_by_event_type_list.append(log_data[events][0][:-1])
    return events_by_event_type_list


print(tabulate(get_events_by_event_type(), headers=columns_list,
               tablefmt='grid'))
