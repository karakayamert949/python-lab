def SSE_val(s,s_app):
    err=0
    for i in range(len(s)):
        err+=(s[i]-s_app[i])**2
    return err
