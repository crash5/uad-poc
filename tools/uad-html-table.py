import json


with open("list/uad_lists.json", "r") as f:
    uad = json.load(f)


print(
    """
 <table border=1>
  <tr>
    <th>id</th>
    <th>desc</th>
    <th>removal</th>
  </tr>
"""
)


def sort_pkgs(removal: str) -> int:
    removal_priority = {"Recommended": 1, "Advanced": 2, "Expert": 3, "Unsafe": 4}
    return removal_priority.get(removal, 99)


for id, infos in sorted(uad.items(), key=lambda x: sort_pkgs(x[1]["removal"])):
    color = ""
    if infos["removal"] == "Unsafe":
        color = "lightsalmon"
    elif infos["removal"] == "Recommended":
        color = "lightgreen"

    print(
        f"""
  <tr bgcolor='{color}'>
    <td><a href='https://play.google.com/store/apps/details?id={id}' target='_blank'>{id}</a></td>
    <td>{infos['description']}</td>
    <td>{infos["removal"]}</td>
  </tr>
    """
    )

print("</table>")
