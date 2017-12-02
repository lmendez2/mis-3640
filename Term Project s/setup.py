import cx_Freeze

executables = [cx_Freeze.Executable("new.py")]

cx_Freeze.setup(
    name = "City Run", options = {"build_exe": {"packages":["pygame"], 
    "include_files": ["man.png","oldm.png","tour.png", "home.png", "homehover.png"]}},
    executables = executables
)