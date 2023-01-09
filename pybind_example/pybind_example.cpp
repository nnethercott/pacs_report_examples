#include <iostream>

class Base
{
public:
    Base(int i) : id(i){};
    virtual int get_id() const
    {
        return id;
    }
    void hi() const
    {
        std::cout << "hi\n";
    }

protected:
    int id;
};

class Derived : public Base
{
public:
    Derived(int i, int j) : Base(i), id2(j){};
    int get_id() const override
    {
        return id2;
    }

private:
    int id2;
};

/*
int main()
{
    Base b{4};
    Derived d{1, 2};
    std::cout << b.get_id() << std::endl;
    std::cout << d.get_id() << std::endl;
}
*/

#include <pybind11/pybind11.h>

namespace py = pybind11;

PYBIND11_MODULE(BaseDerived, m)
{
    py::class_<Base>(m, "Base") // binding the base class object
        .def(py::init<int>())
        .def("say_hi", &Base::hi)
        .def("get_id", &Base::get_id);

    py::class_<Derived, Base>(m, "Derived") // binding derived
        .def(py::init<int, int>())
        .def("get_id", &Derived::get_id);
}
