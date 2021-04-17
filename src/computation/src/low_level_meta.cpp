#include <bits/stdc++.h>

typedef void (*function)(void);
typedef std::map<std::string, function> func_map;


void zero_(){
    std::cout<<0<<std::endl;
}

void one_(){
    std::cout<<1<<std::endl;
}

void two_(){
    std::cout<<2<<std::endl;
}

void three_(){
    std::cout<<3<<std::endl;
}

void four_(){
    std::cout<<4<<std::endl;
}

void five_(){
    std::cout<<5<<std::endl;
}


void caller(func_map &f1_ , const std::string& str){

        auto iter = f1_.find(str);
        (*iter->second)();
}

int main(){

    func_map f1_ = {{"0", &zero_}, {"1", &one_}, {"2", &two_}, {"3", &three_}, {"4", &four_}, {"5", &five_}};
    caller(f1_, "5");
 
}