from langchain_text_splitters import (
    RecursiveCharacterTextSplitter
)

from langchain_community.vectorstores import (
    FAISS
)

from langchain_community.embeddings import (
    HuggingFaceEmbeddings
)

from langchain_core.documents import (
    Document
)


embedding = HuggingFaceEmbeddings(
    model_name="all-MiniLM-L6-v2"
)



def build_vector_db(df):

    docs = []

    for _, row in df.iterrows():

        docs.append(

            Document(

                page_content=str(
                    row.to_dict()
                )

            )

        )


    splitter = (

        RecursiveCharacterTextSplitter(

            chunk_size=500,

            chunk_overlap=50

        )

    )


    split_docs = (

        splitter.split_documents(
            docs
        )

    )


    db = (

        FAISS.from_documents(

            split_docs,

            embedding

        )

    )


    return db




def search_data(

    db,

    query

):

    result = (

        db.similarity_search(

            query,

            k=5

        )

    )


    return "\n".join(

        [

            x.page_content

            for x in result

        ]

    )