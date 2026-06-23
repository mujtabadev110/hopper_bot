from telemetry.plotter import TelemetryPlotter
import glob
import os

def get_latest_csv():
    files = glob.glob("telemetry/*.csv")
    return max(files, key=os.path.getctime)


if __name__ == "__main__":

    csv_file = get_latest_csv()

    plotter = TelemetryPlotter(csv_file)
    plotter.plot_all()