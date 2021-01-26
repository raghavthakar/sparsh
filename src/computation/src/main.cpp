#include <chrono>
#include <functional>
#include <memory>
#include <string>
#include <bits/stdc++.h>
#include "rclcpp/rclcpp.hpp"
#include "std_msgs/msg/string.hpp"
#include "opencv2/imgproc.hpp"
#include "opencv2/highgui.hpp"

using namespace std;
using namespace cv;
/* This example creates a subclass of Node and uses std::bind() to register a
* member function as a callback from the timer. */

class OCR : public rclcpp::Node
{

  private:
	//ROS
    rclcpp::Publisher<std_msgs::msg::String>::SharedPtr publisher_;
	
	
	// ADDRESS ALLOCATION
	std::string address;
	
	std::string address_img;
	
	std::string address_txt;
	
	std::string address_pdf;
	
	std::string file_extension;
	
	std::vector<std::string> address_extension;
	
	//OPENCV
	cv::Mat img, erosion_dst, dilation_dst;

	int erosion_elem = 3;
	
	int erosion_size = 10;
	
	int dilation_elem = 3;
	
	int dilation_size = 10;

	// TXT MANIP
	string str_from_txt_;

  public:
	
	OCR();
	
	
	void address_allocation();
	
	
	void image_manipulation();
	
	
	void txt_manipulation();
	
	
	void pdf_manipulation();
	
	
	void erosion();
	
	
	void dilation();
};

	OCR::OCR(): Node("Sparsh_OCR"), count_(0)
	{
	
		publisher_ = this->create_publisher<std_msgs::msg::String>("topic", 10);
	
	}


	void OCR::address_allocation()
	{
		int pos = address.find(".");
		file_extension = address.substr(pos + 1);

			if (file_extension.compare(address_extension[0]) == 0){
				
				address_img = file_extension
			
			} 
			
			else if (file_extension.compare(address_extension[1]) == 0){
			
				address_txt = file_extension
			
			}   
			
			else if (file_extension.compare(address_extension[2]) == 0){
			
				address_pdf = file_extension
			
			}   

			else{
			
				std::cout<<"FILE EXTENSION NOT SUPPORTED\n";
			
			}

	}

	void OCR::Erosion()
	{
		int erosion_type = cv::MORPH_RECT;

		cv::Mat element = getStructuringElement( erosion_type, Size( 2*erosion_size + 1, 2*erosion_size+1 ), Point( erosion_size, erosion_size ) );
	
		erode( img, erosion_dst, element );

	}

	void OCR::Dilation()
	{
		int dilation_type = cv::MORPH_RECT;

		Mat element = getStructuringElement( dilation_type, Size( 2*dilation_size + 1, 2*dilation_size+1 ), Point( dilation_size, dilation_size ) );
	
		dilate(img, dilation_dst, element );
	}

	void OCR::image_manipulation(){
	
		if( address_img.size()  != 0){
	
			Erosion();
	
			Dilation();
	
			// OCR OUTPUT
		}
	}

	void OCR::txt_manipulation(){
	
		if( address_txt.length != 0){
	
			ifstream file("a.txt");
	
			if(file){
	
				while(getline(file, str_from_txt_, '.')){
	
					cout<<str_from_txt_<<"\n";
	
				}
	
			}

			else{

				cout<<"FILE NOT FOUND\n";

			}
			
		} 
	}

	void
int main(int argc, char * argv[])
  {
    	rclcpp::init(argc, argv);
    	rclcpp::spin(std::make_shared<OCR>());
    	rclcpp::shutdown();
    	return 0;
  }
