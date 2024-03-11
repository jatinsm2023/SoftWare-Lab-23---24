#include <iostream>
#include <vector>
#include <cmath> // Add missing include directive

using namespace std;

class Point
{
    double x, y;

public:
    Point(double x_, double y_) : x(x_), y(y_) {}
    ~Point() {} // Destructor
    double dist(Point &p) const
    {
        return sqrt((x - p.x) * (x - p.x) + (y - p.y) * (y - p.y)); // Fix typo: should be (y - p.y) * (y - p.y)
    }
    double getX() // Fix return type
    {
        return this->x;
    }
    double getY() // Fix return type
    {
        return this->y;
    }
};

class Polygon
{
    vector<Point> v;

public:
    void addPoint(Point &p)
    {
        this->v.push_back(p);
    }

    vector<Point> getVector()
    {
        return this->v;
    }

    void Write()
    {
        cout << "[ ";
        for (int i = 0; i < v.size(); i++)
        {
            cout << "(" << v[i].getX() << "," << v[i].getY() << "),";
        }
        cout << " ]" << endl;
    }
};

int main()
{
    Polygon p;
    int n;
    cin >> n;
    for (int i = 0; i < n; i++)
    {
        double x, y;
        cin >> x >> y;
        Point a(x, y);
        p.addPoint(a);
    }
    p.Write();

    return 0; // Add a return statement to main
}
