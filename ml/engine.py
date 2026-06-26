class StrainAnalysisEngine:
    def __int__(self):
        print("Start working with ML engine")

    def process_video(self, file_path: str) -> dict:
        #temp stub
        print(f"Analyzing file {file_path}")

        return{
            "status": "success",
            "metrics": {
                "global_longitudinal_strain": -18.5,
                "ejetion_fraction": 55.0

            },
            "info": "Speckle tracking completed successfully"
        }