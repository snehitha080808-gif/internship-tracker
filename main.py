import json
try:
    with open("applications.json","r") as file:
        applications = json.load(file)
except FileNotFoundError:
        applications = []
while True:
    print("------JOB & INTERNSHIP TRACKER------")
    print("1.Add Application")
    print("2.View Application")
    print("3.Search Application")
    print("4.Update status")
    print("5.Delete Application")
    print("6.Statistics")
    print("7.Exit")

    choice = input("Enter your choice:")

    if choice == "1":
        company = input("Enter company name:")
        role = input("Enter role :")
        deadline = input("Enter deadline:")
        status = input("Enter status:")

        application = {
            "company": company,
            "role": role,
            "deadline": deadline,
            "status": status
        }

        applications.append(application)
        with open("applications.json","w") as file:
            json.dump(applications,file,indent = 4)
        print("Application added successfully!")

    elif choice == "2":
        if not applications:
            print("No applications found")
        else:
            for app in applications:
                print("--------------------------------------------------------")
                print("Company :",app["company"])
                print("Role :",app["role"])
                print("deadline:",app["deadline"])
                print("status:",app["status"])
                print("--------------------------------------------------------")

    elif choice == "3":
        company_name = input("Enter company name to search:")

        found = False

        for app in applications:
            if app["company"].lower() == company_name.lower():
                print("Application found:")
                print(app)
                found = True
                break

        if not found:
            print("Application not found.")

    elif choice == "4":
        company_name = input("Enter company name:")

        found = False

        for app in applications:
            if app["company"].lower() == company_name.lower():
                new_status = input("Enter new status:")
                app["status"] = new_status
                with open("applications.json","w")as file:
                    json.dump(applications,file,indent = 4)
                print("Status updated successfully!")
                found = True
                break

        if not found:
            print("Application not found.")

    elif choice == "5":
        company_name = input("Enter company name to delete:")

        found = False

        for app in applications:
            if app["company"].lower() == company_name.lower():
                applications.remove(app)
                with open("applications.json","w") as file:
                    json.dump(applications,file,indent = 4)
                print("Application deleted successfully!")
                found = True
                break

        if not found:
            print("Application not found.")

    elif choice == "6":
        total = len(applications)
        applied = 0
        selected = 0
        rejected = 0

        for app in applications:
            status = app["status"].lower()

            if status == "applied":
                applied += 1
            elif status == "selected":
                selected += 1
            elif status == "rejected":
                rejected += 1

        print("Total Applications:", total)
        print("Applied:", applied)
        print("Selected:", selected)
        print("Rejected:", rejected)

    elif choice == "7":
        print("Thank you!")
        break