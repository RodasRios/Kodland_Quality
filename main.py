from modules import data_loading, data_cleaning, data_preprocessing, model_building

def main():
    # Load the dataset
    df_raw = data_loading.load_dataset('/content/gdrive/MyDrive/Colab Notebooks/Ranya_Nico_Projects/Datasets/MENA/MENA_RAW.csv')
    
    # Perform data cleaning
    df_cleaned = data_cleaning.clean_data(df_raw)
    
    # Perform data preprocessing
    df_preprocessed = data_preprocessing.preprocess_data(df_cleaned)
    
    # Build and evaluate the model
    model = model_building.build_model(df_preprocessed)
    model_building.evaluate_model(model, df_preprocessed)

if __name__ == "__main__":
    main()