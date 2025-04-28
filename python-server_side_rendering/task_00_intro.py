import os

def generate_invitations(template: str, attendees: list[dict]):
    if not template:
        print("Template is empty, no output files generated.")
        return

    if not attendees:
        print("No data provided, no output files generated.")
        return

    if not isinstance(template, str):
        print("ERROR: template must be a string")
        return

    if not isinstance(attendees, list) or not all(isinstance(item, dict) for item in attendees):
        print("Error: attendees should be a list of dictionaries.")
        return
    
    for index, attendee in enumerate(attendees, start=1):
        template_content = template
        for key in ['event_title', 'name', 'event_date', 'event_location']:
            placeholder = "{" + f"{key}" + "}"
            value = attendee.get(key) or "N/A"
            template_content = template_content.replace(placeholder, value)
        if not os.path.exists(f"output_{index}.txt"):
            try:
                with open(f"output_{index}.txt", "w") as file:
                    file.write(template_content)
                    print("Successfully written to the {}".format(f"output_{index}.txt"))
            except Exception as e:
                print("Error writing to file {}: {}".format(f"output_{index}.txt)", e))
