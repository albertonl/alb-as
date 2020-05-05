# Aules is for some reason constantly changing versions,
# and that's why I'm adding this

def get_login_url(version):
    """
    Get a valid login URL for a given Aules version.
    2020/05/05: Aules4
    """
    if version == "4" or version == "default":
        # DEFAULT AS OF 2020/05/05: Aules4
        return 'https://aules4.edu.gva.es/moodle/login/index.php'
    elif version == "1" or version == "base":
        return 'https://aules.edu.gva.es/moodle/login/index.php'
    elif version == "2":
        raise RuntimeError("Aules2 has been deprecated. Please try again using either the \"base\" (Aules) or the \"default\" (Aules4) version.")
        # return 'https://aules2.edu.gva.es/moodle/login/index.php'
    else: # it doesn't seem for Aules3 to have ever existed...
        raise RuntimeError(f"Unknown Aules version \"{version}\". Please try again using either the \"base\" (Aules) or the \"default\" version.")

def get_dashboard_url():
    """
    Get a valid dashboard URL for the latest Aules version.
    2020/05/05: Aules4
    """
    return 'https://aules4.edu.gva.es/moodle/my/'


def convert_url(url, mode, version=""):
    """
    Convert a deprecated URL from an old Aules version to the latest one.
    2020/05/05: Aules4
    """
    if mode == "manual":
        if version == "4" or version == "default":
            print(f"URL \'{url}\' already in latest version. Skipping...")
            return url
        elif version == "2":
            return url.replace("aules2.edu.gva.es", "aules4.edu.gva.es")
        elif version == "1" or version == "base":
            return url.replace("aules.edu.gva.es", "aules4.edu.gva.es")
        else:
            raise RuntimeError(f"Unknown Aules version \"{version}\" for manual replacement.")
    elif mode == "auto":
        if "aules4.edu.gva.es" in url:
            # already latest version
            print(f"URL \'{url}\' already in latest version. Skipping...")
            return url
        elif "aules2.edu.gva.es" in url:
            # Aules2
            return url.replace("aules2.edu.gva.es", "aules4.edu.gva.es")
        elif "aules.edu.gva.es" in url:
            # Aules(base)
            return url.replace("aules.edu.gva.es", "aules4.edu.gva.es")
        else:
            raise RuntimeError(f"Unknown Aules version \"{version}\" for automatic replacement.")
