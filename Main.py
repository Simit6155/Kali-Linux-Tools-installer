update = ["sudo", "apt", "update", "&&", "sudo", "apt", "upgrade", "-y"]
subprocess.run(update)

phish_repo = "https://github.com/htr-tech/zphisher.git"
phish_clone = ["git", "clone", phish_repo]
subprocess.run(phish_clone)

cam_repo = "https://github.com/techchipnet/CamPhish.git"
cam_clone = ["git", "clone", cam_repo]
subprocess.run(cam_clone)

repo = "https://github.com/Simit6155/SchimmelBox-Warriors.git"
clone_cmd = ["git", "clone", repo]
subprocess.run(clone_cmd)

repo_simit = "https://github.com/Simit6155/Multi-Tool.git"
clone_cmd_ = ["git", "clone", repo_simit]
subprocess.run(clone_cmd_)

repo_simist = "https://github.com/Simit6155/GeoLocator.git"
clone_cmd_s = ["git", "clone", repo_simist]
subprocess.run(clone_cmd_s)
