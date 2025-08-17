from math import sqrt


def run_k_nearest_neighbor():
    """Run K nearest neighbors against the training and test sets."""
    input_patients = read_training_data("gene_expression_training_set.txt")
    new_patients = read_test_data("gene_expression_test_set.txt")
    prognoses = solve_k_nearest(input_patients, new_patients, k=5)

    # report the prognosis class for each of the new patients
    print("The prognosis class for the new patients when k=5 is as follows: ")
    for prognosis in prognoses:
        print(f"Patient {prognosis}: {prognoses[prognosis]}")



def solve_k_nearest(input_patients, new_patients, k):
    """Read in the input patients as training data to use to determine and report
    the prognosis of the 10 new patients.

    Args:
        input_patients (list of dicts): dictionaries of training patient
            data. see: `read_training_data`

        new_patients (list of dicts): dictionaries of test patient data.
            see: `read_test_data`
        k (int): number of nearest neighbors to use to predict the prognosis
        for an unlabeled patient
    """
    if k % 2 == 0:
        raise ValueError("k must be odd")
    # create a dict storing the prognosis of the 10 new patients
    prognoses = {}
    # create an index/id for each patient
    pat_ind = 1
    for patient in new_patients:
        # create a list storing the distance to each responder
        responder_dist = []
        # create a list storing the distance to each non-responder
        non_resp_dist = []
        # iterate through all input patients and add distance to correct list
        for input in input_patients:
            dist = compute_dist(patient["expression"], input["expression"])
            if input["class"] == "R":
                responder_dist.append(dist)
            else:
                non_resp_dist.append(dist)
        # count variable finds the closest k distances
        count = 0
        # count the number of responders and non-responders in the closest k neighbors
        resp_count = 0
        non_resp_count = 0
        # sort both lists by distance to get the closest neighbors
        responder_dist = sorted(responder_dist)
        non_resp_dist = sorted(non_resp_dist)
        # keep finding the next closest neighbor until you find k neighbors
        while count < k:
            # take the closest responder and non-responder
            resp = responder_dist[0]
            non_resp = non_resp_dist[0]
            # depending on which is closest, increment corresponding count and update list
            # in a case of tied distances, this algorithm chooses the responder first
            if resp <= non_resp:
                resp_count += 1
                responder_dist.pop(0)
            else:
                non_resp_count += 1
                non_resp_dist.pop(0)
            count += 1
        # find which class has the majority vote
        if resp_count > non_resp_count:
            prognoses[pat_ind] = "R"
        else:
            prognoses[pat_ind] = "N"
        pat_ind += 1
    return (prognoses)
    # create a dict storing the class and distance from each expression value to the patient's expression value


def read_training_data(file_name):
    """Read the training gene expression data from a text file. Note: the
    patients in the training data are classified as "R" (responsive to
    treatment) or "N" (non-responsive to treatment).  For example,
    input_patients[0]["class"] = the class of the first patient (R or N)
    input_patients[0]["expression"][0] = the expression of the first
    gene for the first patient.

    Returns:
        (list of dicts): list of patients as a class and expression data. The
        dictionary of each patient will be in the form of:
            'class' -> string with values strictly 'N' or 'R' for
            non-responsive or responsive to the treatment
            'expression' -> list of floats of gene expression values

        and look something like:
            {'class': 'N', 'expression': [9.049, 8.313, ..., 6.428700888]}
    """
    return read_data(file_name, test_data=False)


def read_test_data(file_name):
    """Read the test gene expression data from a text file. Note: the
    patients in the test data are not classified.

   Returns:
    (list of dicts): list of patients as a class and expression data. The
    dictionary of each patient will be in the form of:
        'class' -> string with only 'unknown' as its value
        'expression' -> list of floats of gene expression values

    and look something like:
        {'class': 'unknown', 'expression': [9.049, 8.313, ..., 6.428700888]}
    """
    return read_data(file_name, test_data=True)


def read_data(file_name, test_data=False):
    with open(file_name, "r") as f:
        lines = f.readlines()

    patients = []

    for line in lines:
        line = line.strip()
        data = line.split()  # check that you are splitting on "\t"

        if test_data:
            class_name = "unknown"
        else:
            class_name = data.pop(0)

        float_data = [float(datum) for datum in data]
        patient = {"class": class_name, "expression": float_data}
        patients.append(patient)

    return patients


def compute_dist(tuple_1, tuple_2):
    """Return the Euclidean distance between two points in any number of
    dimensions."""
    
    if len(tuple_1) != len(tuple_2):
        raise ValueError("Cannot compute Euclidean distance between tuples of different sizes!")
    
    dist = 0
    for i in range(len(tuple_1)):
        dist += (tuple_1[i] - tuple_2[i]) * (tuple_1[i] - tuple_2[i])
      
    return sqrt(dist)


if __name__ == "__main__":
    run_k_nearest_neighbor()
