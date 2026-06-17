from utils.career_roadmap import generate_roadmap

roadmap = generate_roadmap(
    "Data Scientist",
    ["statistics", "power bi"]
)

for step in roadmap:
    print(step)