import os


class Config:
    """
    Configuration class to manage file paths and settings for the application.
    """

    # --- PDF Configuration ---
    # Directory where source PDF documents are located.
    PDF_SOURCE_DIRECTORY: str = "data"

    # Directory where ChromaDB embeddings will be persisted.
    CHROMA_PERSIST_DIRECTORY: str = "docs/chroma"

    # --- Embedding Model Configuration ---
    EMBEDDING_MODEL_NAME = "intfloat/multilingual-e5-large"

    CHUNK_SIZE = 2028
    CHUNK_OVERLAP = 250

    def __init__(self):
        # Ensure the PDF source directory exists upon initialization.
        os.makedirs(self.PDF_SOURCE_DIRECTORY, exist_ok=True)

        print(
            f"Configuration loaded. PDF documents should be placed "
            f"in '{self.PDF_SOURCE_DIRECTORY}'."
        )


# Create a global instance of the Config class
config = Config()