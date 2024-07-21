import subprocess, argparse, pyttsx3

parser = argparse.ArgumentParser(
    prog="SubRunner", description="Yust runs script", epilog="End"
)
parser.add_argument("name")
args = parser.parse_args()
subprocess.run(args=["echo", args.name])
engine = pyttsx3.init()
engine.say(text=args.name)
engine.runAndWait()
engine.save_to_file(text=args.name, filename="tts")
