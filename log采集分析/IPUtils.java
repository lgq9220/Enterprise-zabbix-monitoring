package com.smk.b2bpay.util;

import javax.servlet.http.HttpServletRequest;

/**
 * Function: ip工具类 <br/>
 * Date: 2016年7月26日 上午11:19:47 <br/>
 *
 * @author jianghm
 * @version 1.0
 * @Copyright (c) 2016, 杭州市民卡有限公司  All Rights Reserved.
 */
public class IPUtils {
	
	/**
	 * 获取ip
	 * 
	 * @param request
	 * @return
	 */
	public static String getIpAddress(HttpServletRequest request) {
		String ip = request.getHeader("x-forwarded-for"); 
	    if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) { 
	        ip = request.getHeader("Proxy-Client-IP"); 
	    } 
	    if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) { 
	        ip = request.getHeader("WL-Proxy-Client-IP"); 
	    } 
	    if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) { 
	        ip = request.getHeader("HTTP_CLIENT_IP"); 
	    } 
	    if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) { 
	        ip = request.getHeader("HTTP_X_FORWARDED_FOR"); 
	    } 
	    if (ip == null || ip.length() == 0 || "unknown".equalsIgnoreCase(ip)) { 
	        ip = request.getRemoteAddr(); 
	    } 
	    return ip.equals("0:0:0:0:0:0:0:1") ? "127.0.0.1" : ip;
	}
	

}

