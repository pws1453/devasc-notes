import creds
import meraki

def main():
    dashboard = meraki.DashboardAPI()
    orgs = dashboard.organizations.getOrganizations()
    print(orgs)

if __name__ == "__main__":
    main()