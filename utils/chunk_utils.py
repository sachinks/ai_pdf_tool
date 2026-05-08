CHUNK_SIZE = 4000
OVERLAP_SIZE = 500


def chunk_text(text,
               chunk_size=CHUNK_SIZE,
               overlap=OVERLAP_SIZE):
    """
    Split text into overlapping chunks while
    trying to preserve semantic boundaries.
    """

    chunks = []

    start = 0

    while start < len(text):

        end = start + chunk_size

        if end >= len(text):
            chunks.append(text[start:].strip())
            break

        # Try paragraph split
        split_index = text.rfind("\n\n", start, end)

        # Fallback to sentence split
        if split_index == -1:
            split_index = text.rfind(". ", start, end)

        # Worst case fallback
        if split_index == -1:
            split_index = end

        chunk = text[start:split_index].strip()

        chunks.append(chunk)

        # Overlap logic
        start = split_index - overlap

        if start < 0:
            start = 0

    return chunks