def needleman_wunsch(seq_a: str, seq_b: str, match: int, mismatch: int, gap: int) -> tuple[tuple[str, str], int]:
    # Initialzing the the scoring matrix
    rows = len(seq_a) + 1
    cols = len(seq_b) + 1
    score_matrix = [[0] * cols for _ in range(rows)]

    # Initializing the traceback matrix
    traceback_matrix = [[0] * cols for _ in range(rows)]

    # Initialize the scoring
    for i in range(1, rows):
        score_matrix[i][0] = i * gap
    for j in range(1, cols):
        score_matrix[0][j] = j * gap

    # Filling in the scoring matrix and traceback matrix
    for i in range(1, rows):
        for j in range(1, cols):
            match_mismatch_score = match if seq_a[i - 1] == seq_b[j - 1] else mismatch

            # Calculating possible scores using each adjacent cell and adding the max score
            diag_score = score_matrix[i - 1][j - 1] + match_mismatch_score
            up_score = score_matrix[i - 1][j] + gap
            left_score = score_matrix[i][j - 1] + gap
            max_score = max(diag_score, up_score, left_score)
            score_matrix[i][j] = max_score

            if max_score == diag_score:
                traceback_matrix[i][j] = "diag"
            elif max_score == up_score:
                traceback_matrix[i][j] = "up"
            else:
                traceback_matrix[i][j] = "left"

    # Tracing back to find the aligned sequences
    aligned_seq_a = ""
    aligned_seq_b = ""
    i, j = rows - 1, cols - 1
    while i > 0 or j > 0:
        if traceback_matrix[i][j] == "diag":
            aligned_seq_a = seq_a[i - 1] + aligned_seq_a
            aligned_seq_b = seq_b[j - 1] + aligned_seq_b
            i -= 1
            j -= 1
        elif traceback_matrix[i][j] == "up":
            aligned_seq_a = seq_a[i - 1] + aligned_seq_a
            aligned_seq_b = "-" + aligned_seq_b
            i -= 1
        else:
            aligned_seq_a = "-" + aligned_seq_a
            aligned_seq_b = seq_b[j - 1] + aligned_seq_b
            j -= 1

    return (aligned_seq_a, aligned_seq_b), score_matrix[rows - 1][cols - 1]


