import random
import resource
import Body.data
import requests
from locust import HttpUser, task, tag, constant_throughput
from link import url

# resource.setrlimit(resource.RLIMIT_NOFILE, (999999, 999999))
requests.packages.urllib3.disable_warnings()


def settings_time(number):
    if number == 1:
        wait_time = constant_throughput(1)
        return wait_time
    elif number == 2:
        wait_time = constant_throughput(0.1)
        return wait_time


class WebsiteUser(HttpUser):
    Body.data.delete_html()
    wait_time = constant_throughput(1)
    host = url

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.client.verify = False

    @tag('tag1')
    @task
    def company_activity(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/activity',
                         json=Body.data.PAYLOAD_ACTIVITY, headers=Body.data.HEADERS)

    @tag('tag1', 'tag2')
    @task
    def company_affiliated(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/affiliated',
                         json=Body.data.PAGINATION, headers=Body.data.HEADERS)

    @tag('tag1', 'tag3')
    @task
    def company_egrul(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/egrul',
                         headers=Body.data.HEADERS, json=Body.data.PAYLOAD_EGRUL)

    @tag('tag1', 'tag4')
    @task
    def company_company(self):
        self.client.get(f'company/{random.choice(Body.data.company_ogrn())}')

    @tag('tag1', 'tag5')
    @task
    def company_instances(self):
        res = self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/instances',
                               headers=Body.data.HEADERS, json=Body.data.PAYLOAD_INSTANCES)

    @tag('tag1', 'tag6')
    @task
    def company_licenses(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/licenses',
                         headers=Body.data.HEADERS, json=Body.data.PAYLOAD_LICENSES)

    @tag('tag1', 'tag7')
    @task
    def company_predecessors(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/predecessors',
                         headers=Body.data.HEADERS, json=Body.data.PAGINATION)

    @tag('tag1', 'tag8')
    @task
    def company_successors(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/successors',
                         headers=Body.data.HEADERS, json=Body.data.PAGINATION)

    @tag('tag1', 'tag9')
    @task
    def company_participants(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/participants',
                         json=Body.data.PAYLOAD_PARTICIPANTS, headers=Body.data.HEADERS)

    @tag('tag1', 'tag10')
    @task
    def company_msp_support(self):
        self.client.post(f'api/company/{random.choice(Body.data.company_ogrn())}/msp_support',
                         json=Body.data.PAYLOAD_MSP, headers=Body.data.HEADERS)

    @tag('tag1', 'tag11')
    @task
    def company_register(self):
        self.client.get(f'api/company/{random.choice(Body.data.company_ogrn())}/register')

    @tag('tag1', 'tag12')
    @task
    def company_counters(self):
        self.client.get(f'api/company/{random.choice(Body.data.company_ogrn())}/counters')

    @task
    @tag('tag1', 'tag13')
    def company_report_balance(self):
        self.client.get(
            f'api/company/{random.choice(Body.data.company_ogrn())}/reports/balance?year=2010&form_taxation=УСН')

    @tag('tag1', 'tag1')
    @task
    def company_report_financial_results(self):
        self.client.get(f'api/company/{random.choice(Body.data.company_ogrn())}/reports/financial_results?year=2010&form_taxation=УСН')

    @tag('tag1', 'tag15')
    @task
    def company_report_capital_adjustments_and_changes(self):
        self.client.get(
            f'api/company/{random.choice(Body.data.company_ogrn())}/reports/capital_adjustments_and_changes?year=2020&form_taxation=ОСН')

    @tag('tag1', 'tag16')
    @task
    def company_report_capital_flow(self):
        self.client.get(
            f'api/company/{random.choice(Body.data.company_ogrn())}/reports/capital_flow?year=2020&form_taxation=ОСН')

    @tag('tag1', 'tag17')
    @task
    def company_report_targeted_fundraising(self):
        self.client.get(
            f'api/company/{random.choice(Body.data.company_ogrn())}/reports/targeted_fundraising?year=2020&form_taxation=ОСН')

    @tag('tag1', 'tag18')
    @task
    def company_reports(self):
        self.client.get(f'api/company/{random.choice(Body.data.company_ogrn())}/reports')

    @tag('tag1', 'tag19')
    @task
    def company_taxes(self):
        self.client.get(f'api/company/{random.choice(Body.data.company_ogrn())}/taxes')

    @tag('tag1', 'tag20')
    @task
    def company_taxpayers_group(self):
        self.client.get(f'api/company/{random.choice(Body.data.company_ogrn())}/taxpayers_group')

    @tag('tag1', 'tag21')
    @task
    def individual_activity(self):
        self.client.post(f'api/individual/{random.choice(Body.data.ogrnip())}/activity',
                         json=Body.data.PAYLOAD_ACTIVITY, headers=Body.data.HEADERS)

    @tag('tag1', 'tag22')
    @task
    def individual_coowned_companies(self):
        self.client.post(f'api/individual/{random.choice(Body.data.ogrnip())}/coowned_companies',
                         json=Body.data.PAGINATION, headers=Body.data.HEADERS)

    @tag('tag1', 'tag23')
    @task
    def individual_managed_companies(self):
        self.client.post(f'api/individual/{random.choice(Body.data.ogrnip())}/managed_companies',
                         json=Body.data.PAGINATION, headers=Body.data.HEADERS)

    @tag('tag1', 'tag24')
    @task
    def individual_egrip(self):
        self.client.post(f'api/individual/{random.choice(Body.data.ogrnip())}/egrip',
                         json=Body.data.PAYLOAD_EGRIP, headers=Body.data.HEADERS)

    @tag('tag1', 'tag25')
    @task
    def individual_licenses(self):
        self.client.post(f'api/individual/{random.choice(Body.data.ogrnip())}/licenses',
                         json=Body.data.PAYLOAD_LICENSES, headers=Body.data.HEADERS)

    @tag('tag1', 'tag26')
    @task
    def individual_individual(self):
        self.client.get(f'api/individual/{random.choice(Body.data.ogrnip())}/register')

    @tag('tag1', 'tag27')
    @task
    def individual_register(self):
        self.client.get(f'api/individual/{random.choice(Body.data.ogrnip())}/register')

    @tag('tag1', 'tag28')
    @task
    def individual_counters(self):
        self.client.get(f'api/individual/{random.choice(Body.data.ogrnip())}/counters')

    @tag('tag1', 'tag29')
    @task
    def individual_msp_support(self):
        self.client.post(f'api/individual/{random.choice(Body.data.ogrnip())}/msp_support',
                         json=Body.data.PAYLOAD_MSP, headers=Body.data.HEADERS)

    @tag('tag30')
    @task
    def search(self):
        r = self.client.post('search', json=Body.data.PAYLOAD_SEARCH, headers=Body.data.HEADERS)
        with open("error", "w") as file:
            if (r.status_code == 502) or (r.status_code == 502) or (r.status_code == 504) or (r.status_code == 503):
                file.write(f"{r.status_code} {(r.json())}\n")
