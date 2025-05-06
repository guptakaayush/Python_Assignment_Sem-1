lines = admin.readlines()
        for i in range(len(lines)):
            if lines[i].strip().startswith(f"username:{username}"):