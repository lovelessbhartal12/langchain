from langchain_text_splitters import RecursiveCharacterTextSplitter ,Language


code="""
class TransformerEncoderModel(nn.Module):
    def __init__(self, vocab_size, d_model, nhead, num_layers, dim_ff, max_len=500):
        super().__init__()

        self.embedding = nn.Embedding(vocab_size, d_model)
        self.pos_encoder = PositionalEncoding(d_model, max_len)

        encoder_layer = nn.TransformerEncoderLayer(
            d_model=d_model,
            nhead=nhead,
            dim_feedforward=dim_ff,
            dropout=0.1,
            batch_first=True
        )

        self.transformer_encoder = nn.TransformerEncoder(
            encoder_layer,
            num_layers=num_layers
        )

    def forward(self, src):
        
        src shape: (batch_size, seq_len)
        x = self.embedding(src)
        x = self.pos_encoder(x)
        output = self.transformer_encoder(x)
        return outputc"""

splitter=RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON,
    chunk_size=300,
    chunk_overlap=0

)
chunk=splitter.split_text(code)