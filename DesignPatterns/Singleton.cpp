#include <iostream>


class Singleton
{
public:
    static Singleton* getInstance()
    {
        if (instance == 0)
            instance = new Singleton;
        return instance;
    }

private:
    static Singleton* instance;

    Singleton()
    {

    }
};
Singleton* Singleton::instance = 0;

int main()
{

    Singleton* obj1 = Singleton::getInstance();
    Singleton* obj2 = Singleton::getInstance();
    return 0;
}