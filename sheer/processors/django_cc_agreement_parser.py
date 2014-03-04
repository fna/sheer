from utils import run_query


def documents(name, query):
    results = run_query(query)
    if 'results' in results:
        return process_data(results['results'])
    return results


def process_data(data):
    for ndx, value in enumerate(data):
        value['_id'] = value['id']
        # remove fields we're not interested in
        data[ndx] = value
    return data
