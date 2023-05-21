#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

struct Patient {
    string name;
    int priority;

    Patient(const string& n, int p) : name(n), priority(p) {}
};

class MaxHeap {
private:
    vector<Patient> heap;

    void heapifyUp(int index) {
        if (index == 0)
            return;

        int parent = (index - 1) / 2;
        if (heap[parent].priority < heap[index].priority) {
            swap(heap[parent], heap[index]);
            heapifyUp(parent);
        }
    }

    void heapifyDown(int index) {
        int left = 2 * index + 1;
        int right = 2 * index + 2;
        int largest = index;

        if (left < heap.size() && heap[left].priority > heap[largest].priority)
            largest = left;

        if (right < heap.size() && heap[right].priority > heap[largest].priority)
            largest = right;

        if (largest != index) {
            swap(heap[index], heap[largest]);
            heapifyDown(largest);
        }
    }

public:
    void insert(const string& name, int priority) {
        Patient patient(name, priority);
        heap.push_back(patient);
        heapifyUp(heap.size() - 1);
    }

    Patient extractMax() {
        if (heap.empty())
            throw runtime_error("Heap is empty.");

        Patient maxPatient = heap[0];
        heap[0] = heap.back();
        heap.pop_back();
        heapifyDown(0);

        return maxPatient;
    }

    bool isEmpty() {
        return heap.empty();
    }
};

class PriorityQueue {
private:
    MaxHeap maxHeap;

public:
    void enqueue(const string& name, int priority) {
        maxHeap.insert(name, priority);
    }

    Patient dequeue() {
        return maxHeap.extractMax();
    }

    bool isEmpty() {
        return maxHeap.isEmpty();
    }
};

void printPatient(const Patient& patient) {
    cout << "Patient: " << patient.name << " | Priority: " << patient.priority << endl;
}

int main() {
    PriorityQueue pq;

    int numPatients;
    cout << "Enter the number of patients: ";
    cin >> numPatients;

    for (int i = 0; i < numPatients; i++) {
        string name;
        int priority;
        cout << "Enter the name of patient " << i + 1 << ": ";
        cin >> name;
        cout << "Enter the priority of patient " << i + 1 << ": ";
        cin >> priority;
        pq.enqueue(name, priority);
    }

    vector<Patient> patients;
    while (!pq.isEmpty()) {
        patients.push_back(pq.dequeue());
    }

    sort(patients.begin(), patients.end(), [](const Patient& p1, const Patient& p2) {
        return p1.priority < p2.priority;
    });
    for (const Patient& patient : patients) {
        printPatient(patient);
    }

    return 0;
}
