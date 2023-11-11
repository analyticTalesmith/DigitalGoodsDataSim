from sentence_transformers import SentenceTransformer, util

def semantic_array(strings):
    model = SentenceTransformer('all-MiniLM-L6-v2')

    #Compute embedding for list
    embeddings = model.encode(strings, convert_to_tensor=True)

    #Compute cosine-similarities
    cosine_scores = util.cos_sim(embeddings, embeddings)

    #Generate table of weights to be used for "similar purchases"
    weightList = []
    for i in range(len(embeddings)):
        tempCol = []
        for j in range(len(embeddings)):
            tempCol.append(max(0,(cosine_scores[i][j].cpu().numpy()*10)+5))
        weightList.append(tempCol)
    return weightList