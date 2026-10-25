def get_developer_profile():
    return {
        "goal": "Python Full-Stack Developer",
        "current_phase": "Software Engineering Foundations",
        "daily_study_hours": 3,
    }


def main():
    profile = get_developer_profile()

    print("=== Developer Learning Profile ===")
    for key, value in profile.items():
        print(f"{key.replace('_', ' ').title()}: {value}")


if __name__ == "__main__":
    main()