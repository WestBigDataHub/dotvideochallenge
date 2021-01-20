

class Identification:

    def __init__(self, directory_initial, directory_new, video=False):
        self.directory_initial = directory_initial
        self.directory_new = directory_new
        self.video = video
        self.familiarization_phase = False
        self.test_phase = False

    def familiarization (self, n=10):
        """
        :param n: Number of images in each of two sets for judging
        :return: returns true if the familiarization process successfully completed
        """


        return False

    def test (self, n=10):
        """
        :param n: Number of videos per driver that should be shown
        :return: true if successful
        """

        return False

    def accuracy (self):
        """
        :return: the number d' corresponding to accuracy of responses
        """
        assert self.familiarization_phase == True
        assert self.test_phase == True

        # TODO: Implement calculation of d_prime

        d_prime = 0
        return d_prime

    def bias (self):
        """
        :return: criterion C corresponding to response bias
        """
        assert self.familiarization_phase == True
        assert self.test_phase == True

        # TODO: Implement calculation of C

        C = 0
        return C

    def ethnicity (self):
        """
        :return: kl convergence between original ethnicity calculation and new ethnicity calculation
        """

        # TODO: import the kl divergence class and use it to calculate kl

        return 0

    def gender (self):
        """
        :return: kl divergence between original gender calculation and new gender calculation
        """

        return 0

    def age (self):
        """
        :return: kl divergence between original age calculation and new age calculation
        """

        return 0

    def motion_vector(self):
        """
        :return: Analyzes the motion vectors in both the original and returns difference
        """

        return 0

    def canny_edge(self):
        """
        :return: Analyzes motion before and after using canny edge
        """

        # TODO: Implement Alex's method here

        return 0
