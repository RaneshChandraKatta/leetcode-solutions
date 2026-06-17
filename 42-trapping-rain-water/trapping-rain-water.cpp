class Solution {
public:
    int trap(vector<int>& height) {
        int ans = 0;
        stack<int>st;
        int maxiele = INT_MIN;

        for(int i=0;i<height.size();i++){
            if(height[i] >= maxiele){
                // cout<<" height[i]: "<<height[i]<<" maxiele: "<<maxiele<<endl;
                while(!st.empty()){
                    ans += (maxiele-st.top());
                    // cout<<" ans is: "<<ans<<endl;
                    st.pop();
                }
            }
            st.push(height[i]);
            maxiele = max(maxiele,height[i]);
        }

        stack<int>st2;
        int maxiele2 = INT_MIN;
        reverse(height.begin(),height.end());

        for(int i=0;i<height.size();i++){
            if(height[i] > maxiele2){
                while(!st2.empty()){
                    ans += (maxiele2-st2.top());
                    st2.pop();
                }
            }
            st2.push(height[i]);
            maxiele2 = max(maxiele2,height[i]);
        }
        
        return ans;
    }
};